"use strict";(self["webpackChunkmy_database"]=self["webpackChunkmy_database"]||[]).push([[258],{4258:function(e,s,t){t.r(s),t.d(s,{default:function(){return $}});var a=t(6768),o=t(5130),n=t(4232);const i={class:"login-container"},r=(0,a.Lk)("div",{class:"background-animation"},[(0,a.Lk)("div",{class:"gradient-animation"})],-1),l={class:"login-form"},u=(0,a.Lk)("h2",null,"学生成绩管理系统",-1),d={class:"form-group"},p=(0,a.Lk)("option",{value:""},"选择身份",-1),c=["value"],m={class:"form-group"},h=(0,a.Lk)("label",{for:"username"},"账号:",-1),g={class:"form-group"},k=(0,a.Lk)("label",{for:"password"},"密码:",-1),v=(0,a.Lk)("button",{type:"submit",class:"submit-btn"},"登录",-1),y=(0,a.Lk)("audio",{src:"https://zj.v.api.aa1.cn/api/qqmusic/demo.php?type=3&mid=000puJkK2g6gPk&fid=000puJkK2g6gPk&t=3",autoplay:"",loop:""},null,-1);function b(e,s,t,b,f,L){return(0,a.uX)(),(0,a.CE)("div",i,[r,(0,a.Lk)("div",l,[u,(0,a.Lk)("form",{onSubmit:s[3]||(s[3]=(0,o.D$)(((...e)=>L.login&&L.login(...e)),["prevent"]))},[(0,a.Lk)("div",d,[(0,a.bo)((0,a.Lk)("select",{"onUpdate:modelValue":s[0]||(s[0]=e=>f.identity=e),id:"identity",required:""},[p,((0,a.uX)(!0),(0,a.CE)(a.FK,null,(0,a.pI)(f.identityOptions,(e=>((0,a.uX)(),(0,a.CE)("option",{value:e.value},(0,n.v_)(e.label),9,c)))),256))],512),[[o.u1,f.identity]])]),(0,a.Lk)("div",m,[h,(0,a.bo)((0,a.Lk)("input",{type:"text",id:"username","onUpdate:modelValue":s[1]||(s[1]=e=>f.username=e),required:"",autocomplete:"username"},null,512),[[o.Jo,f.username]])]),(0,a.Lk)("div",g,[k,(0,a.bo)((0,a.Lk)("input",{type:"password",id:"password","onUpdate:modelValue":s[2]||(s[2]=e=>f.password=e),required:"",autocomplete:"current-password"},null,512),[[o.Jo,f.password]])]),v],32)]),y])}t(4114),t(4603),t(7566),t(8721);var f={data(){return{identity:"",identityOptions:[{value:"1",label:"学生"},{value:"2",label:"老师"},{value:"3",label:"管理员"}],username:"",password:""}},methods:{login(){let e=new URLSearchParams;e.append("id",this.identity),e.append("username",this.username),e.append("password",this.password),this.$axios({method:"post",url:"http://127.0.0.1:8687/login",data:e,headers:{"Content-Type":"application/x-www-form-urlencoded;charset=UTF-8"}}).then((e=>{console.log(e.data),this.$message({type:"success",message:e.data.message}),this.$store.dispatch("login",this.username),"1"==this.identity&&this.$router.push("/student/info"),"2"==this.identity&&this.$router.push("/teacher/info"),"3"==this.identity&&this.$router.push("/admin/teacher")})).catch((e=>{this.$message({type:"warning",message:"登录失败！"}),e.response?(console.log(e.response.data),console.log(e.response.status),console.log(e.response.headers)):e.request?console.log(e.request):console.log("Error",e.message),console.log(e.config)}))}}},L=t(1241);const w=(0,L.A)(f,[["render",b]]);var $=w}}]);
//# sourceMappingURL=258.b6c673b1.js.map