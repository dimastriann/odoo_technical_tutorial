# -*- coding: utf-8 -*-
{
    "name": "OWL Framework Tutorial",
    "summary": "OWL Framework Tutorial",
    "author": "Dimas Trian",
    "website": "https://github.com/dimastriann",
    "category": "Hidden",
    "version": "17.0.1.0.0",
    "depends": ["web"],
    "data": [
        # 'security/ir.model.access.csv',
        # "views/views.xml",
        "views/app_templates.xml",
    ],
    "demo": [],
    "installable": True,
    "license": "AGPL-3",
    "assets": {
        "web.assets_backend": [
            # "owl_framework_tutorial/static/src/views/components/my_components.js",
            # "owl_framework_tutorial/static/src/views/components/my_components.xml",
        ],
        "owl_framework_tutorial.app_assets": [
            ("include", "web._assets_core"),
            "web/static/src/module_loader.js",
            "owl_framework_tutorial/static/src/app/new_app.js",
            "owl_framework_tutorial/static/src/app/new_app_page.xml",
        ],
    },
}
