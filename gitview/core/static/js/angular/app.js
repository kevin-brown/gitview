"use strict";

var GitView = {
    app: angular.module("gitView", ["gitView.core", "gitView.repositories"]),
    core: angular.module("gitView.core", ["ngRoute", "timeAgo"]),
    repositories: angular.module("gitView.repositories", [])
}

GitView.app.config([
    "$routeProvider", "$locationProvider",
    function ($routeProvider, $locationProvider) {
        $routeProvider
            .when("/:ownerName/:repositoryName", {
                templateUrl: "/static/views/repository/index.html",
                controller: "RepositoryController"
            })
            .when("/:ownerName/:repositoryName/tree/:treeName", {
                templateUrl: "/static/views/repository/index.html",
                controller: "RepositoryController"
            })
            .when("/:ownerName/:repositoryName/tree/:treeName/:treePath*", {
                templateUrl: "/static/views/repository/index.html",
                controller: "RepositoryController"
            })
            .when("/:ownerName/:repositoryName/commits", {
                templateUrl: "/static/views/repository/index.html",
                controller: "CommitListController"
            })
            .when("/:ownerName/:repositoryName/commits/:treeName", {
                templateUrl: "/static/views/repository/index.html",
                controller: "CommitListController"
            })
            .otherwise({
                resolve: {
                    wtf: function () {
                        // Let Django handle unregistered routes
                        window.location.reload();
                    }
                }
            });
        $locationProvider.html5Mode(true);
    }]);
