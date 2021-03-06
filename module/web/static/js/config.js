// Sets the require.js configuration for your application.
require.config({

    // XXX: To many dots in file breaks dependencies
    paths: {

        jquery: "libs/jquery-1.8.3",
        jqueryui: "libs/jqueryui",
        flot: "libs/jquery.flot-1.1",
        transit: "libs/jquery.transit-0.9.9",
        omniwindow: "libs/jquery.omniwindow",
        bootstrap: "libs/bootstrap-2.2.2",

        underscore: "libs/lodash-1.0.rc3",
        backbone: "libs/backbone-0.9.9",
        wreqr: "libs/backbone.wreqr-0.1.0",
        handlebars: "libs/Handlebars-1.0rc1",

        // Plugins
        text: "libs/text-2.0.3",
        tpl: "../../templates"

    },

    // Sets the configuration for your third party scripts that are not AMD compatible
    shim: {

        "backbone": {
            deps: ["underscore", "jquery"],
            exports: "Backbone"  //attaches "Backbone" to the window object
        },
        "flot": ["jquery"],
        "transit": ["jquery"],
        "omniwindow": ["jquery"],
        "bootstrap": ["jquery"]
    } // end Shim Configuration
});