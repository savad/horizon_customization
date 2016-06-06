from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import tabs

from openstack_dashboard import api
from openstack_dashboard.dashboards.mydashboard.neutronpanel import tables


class NeutronPortsTab(tabs.TableTab):
    name = _("Instances Tab")
    slug = "instances_tab"
    table_classes = (tables.InstancesTable,)
    template_name = ("horizon/common/_detail_table.html")
    preload = False

    def has_more_data(self, table):
        return self._has_more

    def get_instances_data(self):
        try:
            marker = self.request.GET.get(
                        tables.InstancesTable._meta.pagination_param, None)
            instances = api.neutron.port_list(
                self.request,
                )
            self._has_more = None
            print instances, "dddddddddddddddddddddddddddddddddddddddd"
            return instances
        except Exception:
            self._has_more = False
            error_message = _('Unable to get ports')
            exceptions.handle(self.request, error_message)

            return []


class NeutronPanelTabs(tabs.TabGroup):
    slug = "neutron_panel_tabs"
    tabs = (NeutronPortsTab, )
    sticky = True
