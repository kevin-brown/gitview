GitView.repositories.factory("Repository",
["Commit", "$http", "$q", function(Commit, $http, $q)
 {
     function Repository(ownerName, repositoryName, request)
     {
         var self = this;

         self._request = request;

         var loadedPromise = $q.defer();
         self.loaded = loadedPromise.promise;

         self.owner = ownerName;

         self.ownerUrl =  "/" + ownerName + "/";
         self.rootUrl = self.ownerUrl + repositoryName + "/";
         self.filesUrl = self.rootUrl;
         self.commitsUrl = self.rootUrl + "commits";
         self.issuesUrl = self.rootUrl + "issues";
         self.settingsUrl = self.rootUrl + "settings";

         self.apiUrl = "/api/repositories" + self.rootUrl;

         request.then(function (response)
         {
             self.name = response.data.name;
             self.isPublic = response.data.is_public;
             self.hasIssues = response.data.has_issues;
             self.defaultBranch = response.data.default_branch;

             loadedPromise.resolve(response);
         });
     }

     Repository.prototype.getCommit = function (hash)
     {
         var self = this;

         request = $http.get(self.apiUrl + "commits/" + hash);

         request.then(function (response)
         {
             self.commit = response.data;
         });

         return request;
     };

     Repository.prototype.getCommits = function (branch)
     {
         var self = this;

         request = $http.get(self.apiUrl + "commits/" + branch);

         request.then(function (response)
         {
             self.commits = response.data;
             $.each(self.commits, function (dayIndex, day)
             {
                 $.each(day.commits, function (commitIndex, commit)
                 {
                     day.commits[commitIndex] = Commit.parse(self, commit);
                 });
             });
         });

         return request;
     };

     Repository.prototype.getTree = function (tree, treePath)
     {
         var self = this;

         self.tree = true;

         var url = self.apiUrl + "trees/" + tree;

         if (treePath)
         {
             url = url + "/" + treePath;
         }

         request = $http.get(url).then(function (response)
         {
             self.tree = response.data;

             self.tree.commit = Commit.get(self, response.data.commit_hash);

             $.each(self.tree.trees, function ()
             {
                 this.commit = Commit.get(self, this.commit_hash);
             });

             $.each(self.tree.blobs, function ()
             {
                 this.commit = Commit.get(self, this.commit_hash);
             });
         });

         return request;
     };

     var repository = {
         get: function(ownerName, repositoryName) {
             request = $http.get("/api/repositories/" + ownerName + "/" +
                                 repositoryName);

             return new Repository(ownerName, repositoryName, request);
         }
     };

     return repository;
 }]);


GitView.repositories.factory("Commit",
[function()
 {
     function Commit(repository, hash, request, data)
     {
         var self = this;

         if (request)
         {
             request.then(function(response)
             {
                 parse(response.data);
             });
         } else if (data)
         {
             parse(data);
         }

         function parse(data)
         {
             self.hash = data.hash;
             self.shortHash = data.short_hash;

             self.summary = data.summary;
             self.description = data.description;

             self.committedTime = data.committed_time;

             self.commitUrl = repository.rootUrl + "commits/" +
                 self.hash;
             self.treeUrl = repository.rootUrl + "tree/" + self.hash;
         }
     }

     var commit = {
         get: function(repository, hash) {
             request = repository.getCommit(hash);

             return new Commit(repository, hash, request);
         },
         parse: function(repository, commit) {
             return new Commit(repository, null, null, commit);
         }
     };

     return commit;
 }]);
