/** @odoo-module **/

import {registry} from "@web/core/registry";
import {Component} from "@odoo/owl";


export class MyComponentField extends Component {

    setup(){
        super.setup(...arguments)
        console.log(this)
    }
}
MyComponentField.template = "My.Component"

export const myComponentField = {
    component: MyComponentField,
    displayName: "My Component Field",
    supportedTypes: ["char"],
}

registry.category("fields").add("my_component_field", myComponentField);
