"use strict";(self.webpackChunkvite_ml_platform=self.webpackChunkvite_ml_platform||[]).push([[126],{13126:function(e,s,t){t.r(s),t.d(s,{default:function(){return Z}});var r=t(4942),n=t(1413),a=t(29439),l=t(72791),i=t(31776),d=t(64880),c=t(23695),o=t(50273),h=t(66106),u=t(30914),x=t(20135),p=t(87309),j=t(80184),m={padding:"8px 0",display:"flex",alignItems:"center"};function Z(){var e=(0,d.k6)(),s=(0,l.useState)({scene_name:"",scene_desc:"",owner_rtxs:"",bid:"",tid:"",report_field:""}),t=(0,a.Z)(s,2),Z=t[0],g=t[1],y=(0,l.useState)(""),f=(0,a.Z)(y,2),w=f[0],v=f[1];function _(e){return function(s){g((0,n.Z)((0,n.Z)({},Z),{},(0,r.Z)({},e,s.target.value)))}}return(0,l.useEffect)((function(){var s={};e.location.state?(s=e.location.state,sessionStorage.setItem("NationalkaraokeKeyID",JSON.stringify(s)),v(s)):(s=JSON.parse(sessionStorage.getItem("NationalkaraokeKeyID")||""),v(s))}),[]),(0,j.jsx)("div",{className:"SceneRegistrationClass",children:(0,j.jsxs)("div",{className:"bodyClass",children:[(0,j.jsx)("div",{className:"SceneHeader",children:"\u573a\u666f\u6ce8\u518c"}),(0,j.jsxs)("div",{className:"site-card-border-less-wrapper",children:[(0,j.jsx)(o.Z,{title:"\u57fa\u672c\u4fe1\u606f",bordered:!1,children:(0,j.jsxs)(h.Z,{gutter:16,children:[(0,j.jsx)(u.Z,{className:"gutter-row",span:12,children:(0,j.jsxs)("div",{style:m,children:[(0,j.jsx)("span",{style:{width:"26%"},children:"\u573a\u666f\u82f1\u6587\u540d"}),(0,j.jsx)(x.Z,{placeholder:"\u8bf7\u8f93\u5165\u573a\u666f\u82f1\u6587\u540d",style:{width:160},value:Z.scene_name,onChange:_("scene_name")})]})}),(0,j.jsx)(u.Z,{className:"gutter-row",span:12,children:(0,j.jsxs)("div",{style:m,children:[(0,j.jsx)("span",{style:{width:"26%"},children:"\u573a\u666f\u4e2d\u6587\u540d"}),(0,j.jsx)(x.Z,{placeholder:"\u8bf7\u8f93\u5165\u573a\u666f\u4e2d\u6587\u540d",style:{width:160},value:Z.scene_desc,onChange:_("scene_desc")})]})}),(0,j.jsx)(u.Z,{className:"gutter-row",span:12,children:(0,j.jsxs)("div",{style:m,children:[(0,j.jsx)("span",{style:{width:"26%"},children:"\u8d23\u4efb\u4eba"}),(0,j.jsx)(x.Z,{placeholder:"\u8bf7\u8f93\u5165\u8d23\u4efb\u4eba",style:{width:160},value:Z.owner_rtxs,onChange:_("owner_rtxs")})]})})]})}),(0,j.jsx)(o.Z,{title:"\u573a\u666f\u4e0a\u62a5\u4fe1\u606f",bordered:!1,children:(0,j.jsxs)(h.Z,{gutter:16,children:[(0,j.jsx)(u.Z,{className:"gutter-row",span:12,children:(0,j.jsxs)("div",{style:m,children:[(0,j.jsx)("span",{style:{width:"26%"},children:"bid"}),(0,j.jsx)(x.Z,{placeholder:"\u8bf7\u8f93\u5165bid",style:{width:160},value:Z.bid,onChange:_("bid")})]})}),(0,j.jsx)(u.Z,{className:"gutter-row",span:12,children:(0,j.jsxs)("div",{style:m,children:[(0,j.jsx)("span",{style:{width:"26%"},children:"tid"}),(0,j.jsx)(x.Z,{placeholder:"\u8bf7\u8f93\u5165tid",style:{width:160},value:Z.tid,onChange:_("tid")})]})}),(0,j.jsx)(u.Z,{className:"gutter-row",span:12,children:(0,j.jsxs)("div",{style:m,children:[(0,j.jsx)("span",{style:{width:"26%"},children:"\u4e0a\u62a5\u5b57\u6bb5"}),(0,j.jsx)(x.Z,{placeholder:"\u8bf7\u8f93\u5165\u4e0a\u62a5\u5b57\u6bb5",style:{width:160},value:Z.report_field,onChange:_("report_field")})]})})]})}),(0,j.jsx)(p.Z,{type:"primary",className:"preservationClass",onClick:function(){var s=(0,n.Z)((0,n.Z)({},Z),{},{business:w});i.Z.featureRegisterScenePostQuest(s).then((function(s){0===s.retcode?(c.ZP.success("\u573a\u666f\u6ce8\u518c\u6210\u529f"),sessionStorage.setItem("keyID",JSON.stringify(s.result.data)),e.push({pathname:"/HeterogeneousPlatform/Nationalkaraoke/SceneModelInformation",state:(0,n.Z)((0,n.Z)({},s.result.data),{},{ReFeatureInformationTitle:"\u573a\u666f\u6a21\u578b\u914d\u7f6e\u4fe1\u606f"})}),g({scene_name:"",scene_desc:"",owner_rtxs:"",bid:"",tid:"",report_field:""})):s.retmsg&&c.ZP.error("\u5931\u8d25\u539f\u56e0: ".concat(s.retmsg))}))},children:"\u4fdd\u5b58"})]})]})})}}}]);