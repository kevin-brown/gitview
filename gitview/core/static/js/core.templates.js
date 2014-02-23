Ember.TEMPLATES["application"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [4,'>= 1.0.0'];
helpers = this.merge(helpers, Ember.Handlebars.helpers); data = data || {};
  var buffer = '', stack1, helper, options, escapeExpression=this.escapeExpression, helperMissing=helpers.helperMissing, self=this;

function program1(depth0,data) {
  
  var buffer = '';
  data.buffer.push("\n        <ul class=\"nav navbar-nav navbar-right\">\n          <li>\n            <a href=\"/admin/\">\n            admin\n            </a>\n          </li>\n          <li>\n            <a href=\"#\">\n              <i class=\"icon-cog\"></i>\n              Settings\n            </a>\n          </li>\n          <li>\n            <a ");
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "invalidateSession", {hash:{},hashTypes:{},hashContexts:{},contexts:[depth0],types:["STRING"],data:data})));
  data.buffer.push(">\n              <i class=\"icon-signout\"></i>\n              Log out\n            </a>\n          </li>\n        </ul>\n      ");
  return buffer;
  }

function program3(depth0,data) {
  
  var buffer = '';
  data.buffer.push("\n        <ul class=\"nav navbar-nav navbar-right\">\n          <li>\n            <a ");
  data.buffer.push(escapeExpression(helpers.action.call(depth0, "authenticateSession", {hash:{},hashTypes:{},hashContexts:{},contexts:[depth0],types:["STRING"],data:data})));
  data.buffer.push(">\n              <i class=\"icon-signin\"></i>\n              Login\n            </a>\n          </li>\n        </ul>\n      ");
  return buffer;
  }

  data.buffer.push(escapeExpression((helper = helpers['bs-notifications'] || (depth0 && depth0['bs-notifications']),options={hash:{
    'style': ("z-index: 1000; position: fixed; width: 50%; left: 0; right: 0; margin-left: auto; margin-right: auto; margin-top: 50px;")
  },hashTypes:{'style': "STRING"},hashContexts:{'style': depth0},contexts:[],types:[],data:data},helper ? helper.call(depth0, options) : helperMissing.call(depth0, "bs-notifications", options))));
  data.buffer.push("\n\n<nav class=\"navbar navbar-default\" role=\"navigation\">\n  <div class=\"container\">\n    <div class=\"navbar-header\">\n      <button type=\"button\" class=\"navbar-toggle\"\n        data-toggle=\"collapse\"\n        data-target=\".navbar-primary-collapse\">\n        <span class=\"sr-only\">Toggle navigation</span>\n        <span class=\"icon-bar\"></span>\n        <span class=\"icon-bar\"></span>\n        <span class=\"icon-bar\"></span>\n      </button>\n      <a class=\"navbar-brand\" href=\"/\">\n      GitView\n      </a>\n    </div>\n\n    <div class=\"collapse navbar-collapse navbar-primary-collapse\">\n      <ul class=\"nav navbar-nav\">\n        <li><a href=\"#\">Notifications</a></li>\n        <li><a href=\"/admin/\">Admin</a></li>\n      </ul>\n\n      ");
  stack1 = helpers['if'].call(depth0, "session.isAuthenticated", {hash:{},hashTypes:{},hashContexts:{},inverse:self.program(3, program3, data),fn:self.program(1, program1, data),contexts:[depth0],types:["ID"],data:data});
  if(stack1 || stack1 === 0) { data.buffer.push(stack1); }
  data.buffer.push("\n    </div>\n  </div>\n</nav>\n\n<div class=\"container\">\n  ");
  stack1 = helpers._triageMustache.call(depth0, "outlet", {hash:{},hashTypes:{},hashContexts:{},contexts:[depth0],types:["ID"],data:data});
  if(stack1 || stack1 === 0) { data.buffer.push(stack1); }
  data.buffer.push("\n</div>\n");
  return buffer;
  
});