GitView.repositories.controller("RepositoryController",
["Repository", "$scope", "$rootScope", "$http", "$log", "$routeParams",
 function(Repository, $scope, $rootScope, $http, $log, $routeParams)
 {
     $scope.repository = Repository.get($routeParams.ownerName,
                                        $routeParams.repositoryName);

     var breadcrumbs = [];

     if ("treePath" in $routeParams)
     {
         $scope.repository.getTree($routeParams.treeName,
                                   $routeParams.treePath);

         $scope.repository.loaded.then(function ()
         {
             var path = $routeParams.treePath.split("/");

             $.each(path, function (idx, elem)
                    {
                        var pathSplice = path.slice(0, idx + 1);

                        var urlPath = pathSplice.join("/");
                        var treePath = "tree/" + $routeParams.treeName + "/";

                        var url = $scope.repository.filesUrl + treePath +
                            urlPath;

                        var breadcrumb = {
                            title: elem,
                            url: url
                        };

                        $log.log(path, pathSplice, urlPath, url);

                        breadcrumbs.push(breadcrumb);
                    });

             $rootScope.breadcrumbsExtra = breadcrumbs;
         });
     } else if ("treeName" in $routeParams)
     {
         $scope.repository.getTree($routeParams.treeName);
     } else
     {
         $scope.repository.loaded.then(function ()
         {
             $scope.repository.getTree($scope.repository
                                       .defaultBranch);
         });
     }

     $rootScope.breadcrumbsExtra = breadcrumbs;

     $scope.repositoryTemplate = "/static/views/repository/tree.html";
 }]);

GitView.repositories.controller("CommitListController",
["Repository", "$rootScope", "$scope", "$http", "$log", "$routeParams",
 "$window",
 function(Repository, $rootScope, $scope, $http, $log, $routeParams, $window)
 {
     $scope.repository = Repository.get($routeParams.ownerName,
                                        $routeParams.repositoryName);

     var branch = undefined;

     $rootScope.breadcrumbsExtra = [];

     if ("treeName" in $routeParams)
     {
         branch = $routeParams.treeName;
     }

     $scope.repository.loaded.then(function ()
     {
         if (!branch)
         {
             branch = $scope.repository.defaultBranch;
         }

         var commits = $scope.repository.getCommits(branch);

         commits.then(function (response) {
             if (!response.data.length)
             {
                 $window.location.reload();
             }
         });
     });

     $scope.repository.loaded.then(function () {
         $rootScope.breadcrumbsExtra = [
             {
                 title: "Commits",
                 url: $scope.repository.commitsUrl
             }
         ];
     });

     $scope.repositoryTemplate = "/static/views/repository/commits.html";
 }]);

GitView.repositories.controller("CommitInfoController",
["Commit", "$scope",
 function(Commit, $scope)
 {
     $scope.$watch("hash", function ()
     {
         if (!$scope.hash)
         {
             return;
         }

         $scope.commit = Commit.get($scope.repository, $scope.hash);
     });
 }]);

GitView.repositories.controller("RepositoryBreadcrumbsController",
["Commit", "$rootScope", "$scope",
 function(Commit, $rootScope, $scope)
 {
     $scope.breadcrumbs = [];

     $scope.repository.loaded.then(function () {
         $rootScope.$watch("breadcrumbsExtra", function () {
             $scope.breadcrumbs = [
                 {
                     title: $scope.repository.owner,
                     url: $scope.repository.ownerUrl
                 },
                 {
                     title: $scope.repository.name,
                     url: $scope.repository.rootUrl
                 }
             ];

             $scope.breadcrumbs = $.merge($scope.breadcrumbs,
                                          $rootScope.breadcrumbsExtra || []);
         });
     });
 }]);
