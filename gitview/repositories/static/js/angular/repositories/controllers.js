GitView.repositories.controller("RepositoryController",
["Repository", "$scope", "$http", "$log", "$routeParams",
 function(Repository, $scope, $http, $log, $routeParams)
 {
     $scope.repository = Repository.get($routeParams.ownerName, $routeParams.repositoryName);

     if ("treePath" in $routeParams)
     {
         $scope.repository.getTree($routeParams.treeName,
                                   $routeParams.treePath);
     } else if ("treeName" in $routeParams)
     {
         $scope.repository.getTree($routeParams.treeName);
     } else
     {
         $scope.repository.loaded.then(function ()
         {
             $scope.repository.getTree($scope.repository.defaultBranch);
         });
     }

     $scope.repositoryTemplate = "/static/views/repository/tree.html";
 }]);

GitView.repositories.controller("CommitListController",
["Repository", "$scope", "$http", "$log", "$routeParams",
 function(Repository, $scope, $http, $log, $routeParams)
 {
     $scope.repository = Repository.get($routeParams.ownerName, $routeParams.repositoryName);

     var branch = undefined;

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

         $scope.repository.getCommits(branch);
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
