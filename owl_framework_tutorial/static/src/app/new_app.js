/** @odoo-module **/

import { templates} from "@web/core/assets";
import { Component, App, whenReady, xml } from "@odoo/owl";
import {makeEnv, startServices} from "@web/env";

export class MenuComponent extends Component {}
MenuComponent.template = "MenuComponent";

export class MenuComponent2 extends Component {}
MenuComponent2.template = "MenuComponent2";


export class MyFirstComponent extends Component {

    static template = "MyFirstComponent";
    setup(){
        super.setup()
        this.my_prop = false;
    }

    click(){
        console.log(this)
    }
}
// MyFirstComponent.template = "";


export class MyRootComponent extends Component {}
MyRootComponent.template = "MyRootComponent";
MyRootComponent.components = {
    MenuComponent, MenuComponent2, MyFirstComponent
};
//
(async function startNewApp() {
    const env = makeEnv()
    await startServices(env)
    await whenReady()
    const app = new App(
        MyRootComponent,
        {
            name: "New OWL App",
            env,
            templates,
            props: {}
        }
    )
    const root = await app.mount(document.body)
    odoo.__WOWL_DEBUG__ = { root };
})();
