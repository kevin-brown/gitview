Ember.TEMPLATES["application"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [4,'>= 1.0.0'];
helpers = this.merge(helpers, Ember.Handlebars.helpers); data = data || {};
  var buffer = '', stack1, helper, options, helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression;


  data.buffer.push(escapeExpression((helper = helpers['bs-notifications'] || (depth0 && depth0['bs-notifications']),options={hash:{
    'style': ("z-index: 1000; position: fixed; width: 50%; left: 0; right: 0; margin-left: auto; margin-right: auto; margin-top: 50px;")
  },hashTypes:{'style': "STRING"},hashContexts:{'style': depth0},contexts:[],types:[],data:data},helper ? helper.call(depth0, options) : helperMissing.call(depth0, "bs-notifications", options))));
  data.buffer.push("\n\n<nav class=\"navbar navbar-default\" role=\"navigation\">\n  <div class=\"container\">\n    <div class=\"navbar-header\">\n      <button type=\"button\" class=\"navbar-toggle\"\n        data-toggle=\"collapse\"\n        data-target=\".navbar-primary-collapse\">\n        <span class=\"sr-only\">Toggle navigation</span>\n        <span class=\"icon-bar\"></span>\n        <span class=\"icon-bar\"></span>\n        <span class=\"icon-bar\"></span>\n      </button>\n      <a class=\"navbar-brand\" href=\"/\">\n      GitView\n      </a>\n    </div>\n\n    <div class=\"collapse navbar-collapse navbar-primary-collapse\">\n      <ul class=\"nav navbar-nav\">\n        <li><a href=\"#\">Notifications</a></li>\n        <li><a href=\"/admin/\">Admin</a></li>\n      </ul>\n\n      <ul class=\"nav navbar-nav navbar-right\">\n        <li>\n          <a href=\"/admin/\">\n          admin\n          </a>\n        </li>\n        <li>\n          <a href=\"#\">\n            <i class=\"icon-cog\"></i>\n            Settings\n          </a>\n        </li>\n        <li>\n          <a href=\"/logout/\">\n          <i class=\"icon-signout\"></i>\n          Log out\n          </a>\n        </li>\n      </ul>\n    </div>\n  </div>\n</nav>\n\n<div class=\"container\">\n  ");
  stack1 = helpers._triageMustache.call(depth0, "outlet", {hash:{},hashTypes:{},hashContexts:{},contexts:[depth0],types:["ID"],data:data});
  if(stack1 || stack1 === 0) { data.buffer.push(stack1); }
  data.buffer.push("\n</div>\n");
  return buffer;
  
});