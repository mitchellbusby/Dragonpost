// Main Angular JS module.

(function() {

    // Module setup.
    var app = angular.module("app", []);

    // Module configuration.
    // We're changing {{}} to {[]} to avoid conflicts with Jinja2.
    app.config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('{[');
        $interpolateProvider.endSymbol(']}');
    });

}).call()