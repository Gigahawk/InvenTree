"""sample of a broken python file that will be ignored on import"""
from plugin import IntegrationPluginBase


class BrokenIntegrationPlugin(IntegrationPluginBase):
    """
    An very broken integration plugin
    """


aaa = bb  # noqa: F821
