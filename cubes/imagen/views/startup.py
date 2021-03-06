# -*- coding: utf-8 -*-
# copyright 2013-2016 CEA, all rights reserved.
# contact http://i2bm.cea.fr/drf/i2bm/NeuroSpin -- mailto:imagendatabase@cea.fr
#
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html
# for details.

"""cubicweb-neurospinweb views/forms/actions/components for web ui"""
import os
from cubes.piws.views.startup   import (PIWSIndexView, PIWSCardView)
from cubicweb.web.views.startup import IndexView


###############################################################################
# Index View
###############################################################################
class ImagenIndexView(IndexView):

    def call(self, **kwargs):
        """ Class that defines the imagen index view.
        """

        # Must execute an rql to display index properly
        self._cw.execute('Any S Where S is Subject')
        
        ajaxcallback = "get_questionnaires_data"
        rql_labels = ("DISTINCT Any T ORDERBY T WHERE A is Assessment, "
                      "A timepoint T")
        
        QCcentral_url = self._cw.build_url(
                            "view", vid="jtable-table",
                            rql_labels=rql_labels, ajaxcallback=ajaxcallback,
                            title="All Questionnaires", elts_to_sort=["ID"],
                            tooltip_name="All Questionnaires", qtype="QC central")

        resources = {
            "demo-url": "",
            "welcome-url": self._cw.build_url("view",
                                              rql="Any S Where S is Subject"),
            "QCcentral-url": QCcentral_url,
            "license-url": self._cw.build_url("license"),
            "connect-image": self._cw.data_url("images/connect.jpg"),
            "database-image": self._cw.data_url("images/database.jpg"),
            "imagen-image": self._cw.data_url("images/imagen.jpg"),
            "imagen-url": "http://www.imagen-europe.com/",
        }
        views_path = os.path.dirname(os.path.realpath(__file__))
        imagen_cube_path = os.path.split(views_path)[0]
        index_html_path = os.path.join(imagen_cube_path,
                                       'migration',
                                       'static_pages',
                                       'index.html')
        with open(index_html_path) as f:
            html = f.read()

        self.w(html % resources)


###############################################################################
# Registry
###############################################################################
def registration_callback(vreg):
    vreg.register(ImagenIndexView)
    vreg.unregister(PIWSIndexView)
    vreg.unregister(PIWSCardView)
