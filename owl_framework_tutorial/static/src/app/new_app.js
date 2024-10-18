/** @odoo-module **/

import { templates} from "@web/core/assets";
import {
    Component,
    App,
    whenReady,
    onWillDestroy
} from "@odoo/owl";
import {makeEnv, startServices} from "@web/env";

export class MenuComponent extends Component {}
MenuComponent.template = "MenuComponent";

export class MenuComponent2 extends Component {}
MenuComponent2.template = "MenuComponent2";


export class MyFirstComponent extends Component {

    // static template = "MyFirstComponent";
    setup(){
        super.setup()
        this.my_prop = false;
        this.my_array = [];
    }

    click(){
        console.log('before', this)
        this.my_prop = true;
        this.my_array.push(100)
        console.log(this)
    }
}
MyFirstComponent.template = "MyFirstComponent";
MyFirstComponent.props = {
    counter: {type: Number, optional: true},
    parentName: {type: String, optional: true},
    "*": true,
}
MyFirstComponent.defaultProps = {
    counter: 10,
    parentName: "Parent"
}


export class MyRootComponent extends Component {
    setup(){
        super.setup();
        this.name = "MyRootComponent"
    }
}
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
            dev: env.debug,
            templates,
            props: {}
        }
    )
    const root = await app.mount(document.body)
    odoo.__WOWL_DEBUG__ = { root };
})();
