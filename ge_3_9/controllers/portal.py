from odoo import fields, http, _
from odoo.addons.portal.controllers import portal
from odoo.http import request, Response
from odoo.exceptions import AccessError, MissingError, ValidationError

from odoo.addons.portal.controllers.portal import pager as portal_pager


class CustomerPortal(portal.CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        # TODO Update this to check if registry is shared to public
        values['motorcycle_registry_count'] = request.env['motorcycle.registry'].search_count([])
        return values

    def _get_registry_searchbar_sortings(self):
        return {
            'name': {'label': _('Name'), 'order': 'registry_number'},
        }

    def _prepare_registry_portal_rendering_values(self, page=1, sortby=None, date_begin=None, date_end=None, **kw):

        MotorcycleRegistry = request.env['motorcycle.registry']
        values = self._prepare_portal_layout_values()
        partner = request.env.user.partner_id

        sortby = 'name'

        partner = request.env.user.partner_id
        url = '/my/registries'
        
        # TODO Update Domain filter to use public filtering
        domain = []

        searchbar_sortings = self._get_registry_searchbar_sortings()

        sort_order = searchbar_sortings[sortby]['order']

        pager_values = portal_pager(
            url=url,
            total=MotorcycleRegistry.search_count(domain),
            page=page,
            step=self._items_per_page,
            url_args={'date_begin': date_begin, 'date_end': date_end, 'sortby': sortby},
        )

        registries = MotorcycleRegistry.search(domain, limit=self._items_per_page, offset=pager_values['offset'], order=sort_order)

        # user owned registries show up first
        registries = registries.sorted(key=lambda r: r.owner_id.id != partner.id)

        values.update({
            'date': date_begin,
            'entrys': registries.sudo(),
            'page_name': 'registries',
            'pager': pager_values,
            'default_url': url,
            'searchbar_sortings': searchbar_sortings,
            'sortby': sortby,
            'user': partner,
        })

        return values
    
    @http.route(['/my/registries', '/my/registries/page/<int:page>'], type='http', auth="public", website=True)
    def portal_my_registry(self, **kwargs):
        values = self._prepare_registry_portal_rendering_values(**kwargs)
        request.session['motorcycle_registry_history_ids'] = values['entrys'].ids[:100]
        return request.render("ge_3_9.portal_my_registries", values)
    
    @http.route(['/my/registries/<int:registry_id>'], type='http', auth="public", website=True)
    def portal_my_registry_page(self, registry_id, access_token=None,**kwargs):
        try:
            registry_sudo = self._document_check_access('motorcycle.registry', registry_id, access_token=access_token)
        except (AccessError, MissingError):
            return request.redirect('/my')
        
        values = {
            'motorcycle_registry': registry_sudo,
            'report_type': 'html',
            'res_company': registry_sudo.owner_id.company_id,
        }

        history_session_key = 'motorcycle_registry_history_ids'

        values = self._get_page_view_values(
            registry_sudo, access_token, values, history_session_key, False)

        return request.render("ge_3_9.motorcycle_registry_portal_template", values)