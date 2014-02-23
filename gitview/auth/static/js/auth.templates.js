Ember.TEMPLATES["login"] = Ember.Handlebars.template(function anonymous(Handlebars,depth0,helpers,partials,data) {
this.compilerInfo = [4,'>= 1.0.0'];
helpers = this.merge(helpers, Ember.Handlebars.helpers); data = data || {};
  var buffer = '', stack1, helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression, self=this;

function program1(depth0,data) {
  
  var buffer = '', stack1, helper, options;
  data.buffer.push("\n    <label>\n        Username:\n    </label>\n\n    ");
  data.buffer.push(escapeExpression((helper = helpers.input || (depth0 && depth0.input),options={hash:{
    'type': ("text"),
    'class': ("form-control"),
    'valueBinding': ("view.username")
  },hashTypes:{'type': "STRING",'class': "STRING",'valueBinding': "STRING"},hashContexts:{'type': depth0,'class': depth0,'valueBinding': depth0},contexts:[],types:[],data:data},helper ? helper.call(depth0, options) : helperMissing.call(depth0, "input", options))));
  data.buffer.push("\n\n    <label>\n        Password:\n    </label>\n\n    ");
  data.buffer.push(escapeExpression((helper = helpers.input || (depth0 && depth0.input),options={hash:{
    'type': ("password"),
    'class': ("form-control"),
    'valueBinding': ("view.password")
  },hashTypes:{'type': "STRING",'class': "STRING",'valueBinding': "STRING"},hashContexts:{'type': depth0,'class': depth0,'valueBinding': depth0},contexts:[],types:[],data:data},helper ? helper.call(depth0, options) : helperMissing.call(depth0, "input", options))));
  data.buffer.push("\n\n    ");
  stack1 = (helper = helpers['bs-button'] || (depth0 && depth0['bs-button']),options={hash:{
    'type': ("success")
  },hashTypes:{'type': "STRING"},hashContexts:{'type': depth0},inverse:self.noop,fn:self.program(2, program2, data),contexts:[],types:[],data:data},helper ? helper.call(depth0, options) : helperMissing.call(depth0, "bs-button", options));
  if(stack1 || stack1 === 0) { data.buffer.push(stack1); }
  data.buffer.push("\n");
  return buffer;
  }
function program2(depth0,data) {
  
  
  data.buffer.push("\n        Sign in\n    ");
  }

  stack1 = helpers.view.call(depth0, "GitView.LoginFormView", {hash:{},hashTypes:{},hashContexts:{},inverse:self.noop,fn:self.program(1, program1, data),contexts:[depth0],types:["ID"],data:data});
  if(stack1 || stack1 === 0) { data.buffer.push(stack1); }
  data.buffer.push("\n");
  return buffer;
  
});