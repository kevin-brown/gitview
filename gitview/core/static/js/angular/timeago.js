/*
  Original: https://gist.github.com/JensRantil/5470122

  Modified:
   - Ignores blank times
   - Supports `<time datetime></time>`
   - Uses custom `js-relative-time` class
 */

angular.module('timeAgo', [])
    .directive("jsRelativeTime", function($q) {
        return {
            restrict: "C",
            scope: {
                title: "@",
                datetime: "@"
            },
            link: function(scope, element, attrs) {
                var parsedDate = $q.defer();

                parsedDate.promise.then(function() {
                    jQuery(element).timeago();
                });

                attrs.$observe('datetime', function(newValue) {
                    if (!newValue) return;
                    parsedDate.resolve(newValue);
                });

                attrs.$observe('title', function(newValue) {
                    if (!newValue) return;
                    parsedDate.resolve(newValue);
                });
            }
        };
    });
