__author__ = 'savad'

# The slug of the panel to be added to HORIZON_CONFIG. Required.
PANEL = 'neutron_panel'
# The slug of the dashboard the PANEL associated with. Required.
PANEL_DASHBOARD = 'mydashboard'
# The slug of the panel group the PANEL is associated with.
PANEL_GROUP = 'mygroup'

# Python panel class of the PANEL to be added.
ADD_PANEL = 'openstack_dashboard.dashboards.mydashboard.neutronpanel.panel.NeutronPanel'
