"use strict";

module.exports = function(grunt) {
    // Project configuration.
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        emberTemplates: {
            compile: {
                options: {
                    templateBasePath: /gitview\/(.*)\/static\/js\/templates/
                },
                files: {
                    "gitview/auth/static/js/auth.templates.js": [
                        "gitview/auth/static/js/templates/**/*.hbs",
                    ],
                    "gitview/core/static/js/core.templates.js": [
                        "gitview/core/static/js/templates/**/*.hbs",
                    ]
                }
            }
        },
        watch: {
            emberTemplates: {
                files: "gitview/**/static/js/templates/**/*.hbs",
                tasks: ["emberTemplates", ]
            },
        }
    });

    grunt.loadNpmTasks('grunt-ember-templates');
    grunt.loadNpmTasks('grunt-contrib-watch');

    // Default task(s).
    grunt.registerTask('default', ['emberTemplates']);
};
