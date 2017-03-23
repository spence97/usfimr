from tethys_sdk.base import TethysAppBase, url_map_maker


class UsFloodInundationMapRepository(TethysAppBase):
    """
    Tethys app class for US Flood Inundation Map Repository.
    """

    name = 'US Flood Inundation Map Repository'
    index = 'usfimr:home'
    icon = 'usfimr/images/icon.gif'
    package = 'usfimr'
    root_url = 'usfimr'
    color = '#800000'
    description = 'Place a brief description of your app here.'
    enable_feedback = False
    feedback_emails = []

        
    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (UrlMap(name='home',
                           url='usfimr',
                           controller='usfimr.controllers.home'),
                    UrlMap(name='map',
                           url='usfimr/map',
                           controller='usfimr.controllers.map'),
                    UrlMap(name='info',
                           url='usfimr/info',
                           controller='usfimr.controllers.info'),
        )

        return url_maps