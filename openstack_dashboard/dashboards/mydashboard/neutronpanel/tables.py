from django.utils.translation import ugettext_lazy as _

from horizon import tables


class MyFilterAction(tables.FilterAction):
    name = "myfilter"


class InstancesTable(tables.DataTable):
    id = tables.Column("id", verbose_name=_("Id"))
    name = tables.Column("name", verbose_name=_("Name"))
    mac_address = tables.Column("mac_address", verbose_name=_("Mac Address"))
    fixed_ips = tables.Column("fixed_ips", verbose_name=_(" Fixed IPs"))
    status = tables.Column("status", verbose_name=_("Status"))

    class Meta:
        name = "instances"
        verbose_name = _("Instances")
        table_actions = (MyFilterAction,)
