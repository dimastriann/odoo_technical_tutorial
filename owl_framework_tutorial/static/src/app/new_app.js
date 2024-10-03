/** @odoo-module **/

import { templates} from "@web/core/assets";
import { Component, App } from "@odoo/owl";
import {makeEnv, startServices} from "@web/env";


class MyRootComponent extends Component {}
MyRootComponent.template = "MyRootComponent";

(async function startNewApp() {
    const env = makeEnv()
    await startServices(env)
    const app = new App(
        MyRootComponent,
        {
            name: "New OWL App",
            env,
            templates,
        }
    )
    const root = await app.mount(document.body)
    odoo.__WOWL_DEBUG__ = { root };
})();
