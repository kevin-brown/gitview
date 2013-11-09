GitView.repositories.directive("commitInfo",
function ()
{
    return {
        controller: "CommitInfoController",
        replace: true,
        restrict: "E",
        scope: { repository: "=repository", hash: "=hash" },
        templateUrl: "/static/views/repository/commit_info.html",
        transclude: true
    }
});

GitView.repositories.directive("repositoryBreadcrumbs",
function ()
{
    return {
        controller: "RepositoryBreadcrumbsController",
        replace: true,
        restrict: "E",
        scope: { repository: "=repository" },
        templateUrl: "/static/views/repository/breadcrumbs.html",
        transclude: true
    }
});
