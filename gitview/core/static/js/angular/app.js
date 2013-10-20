"use strict";

var GitView = {
    app: angular.module("gitView", ["gitView.core", "gitView.repositories"]),
    core: angular.module("gitView.core", ["ngRoute", "timeAgo"]),
    repositories: angular.module("gitView.repositories", [])
}

GitView.app.config(function ($routeProvider, $locationProvider) {
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
    $locationProvider.html5Mode(true);
});
