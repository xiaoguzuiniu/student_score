"use strict";(self["webpackChunkmy_database"]=self["webpackChunkmy_database"]||[]).push([[333],{9333:function(e,a,t){t.r(a),t.d(a,{default:function(){return r}});var l=t(6768);const s={slot:"footer",class:"dialog-footer"};function o(e,a,t,o,d,n){const i=(0,l.g2)("el-input"),r=(0,l.g2)("el-form-item"),m=(0,l.g2)("el-button"),c=(0,l.g2)("router-link"),u=(0,l.g2)("el-form"),h=(0,l.g2)("el-table-column"),p=(0,l.g2)("el-table"),b=(0,l.g2)("el-option"),g=(0,l.g2)("el-select"),F=(0,l.g2)("el-dialog");return(0,l.uX)(),(0,l.CE)("div",null,[(0,l.bF)(u,{inline:!0,class:"demo-form-inline"},{default:(0,l.k6)((()=>[(0,l.bF)(r,{label:"学号"},{default:(0,l.k6)((()=>[(0,l.bF)(i,{placeholder:"学号",modelValue:d.sno,"onUpdate:modelValue":a[0]||(a[0]=e=>d.sno=e)},null,8,["modelValue"])])),_:1}),(0,l.bF)(r,null,{default:(0,l.k6)((()=>[(0,l.bF)(m,{type:"primary",onClick:n.query},{default:(0,l.k6)((()=>[(0,l.eW)("查询")])),_:1},8,["onClick"]),(0,l.bF)(m,{type:"primary"},{default:(0,l.k6)((()=>[(0,l.bF)(c,{to:"/admin/createstudent"},{default:(0,l.k6)((()=>[(0,l.eW)("新增学生")])),_:1})])),_:1})])),_:1})])),_:1}),(0,l.bF)(p,{data:d.tableData,border:"",style:{width:"100%"}},{default:(0,l.k6)((()=>[(0,l.bF)(h,{fixed:"",prop:"sno",label:"学号",width:"250"}),(0,l.bF)(h,{prop:"name",label:"姓名",width:"175"}),(0,l.bF)(h,{prop:"sex",label:"性别",width:"120"}),(0,l.bF)(h,{prop:"age",label:"年龄",width:"120"}),(0,l.bF)(h,{prop:"class",label:"班级",width:"120"}),(0,l.bF)(h,{fixed:"right",label:"操作",width:"200"},{default:(0,l.k6)((e=>[(0,l.bF)(m,{onClick:a=>n.confirmRemove(e.row),type:"text",size:"small"},{default:(0,l.k6)((()=>[(0,l.eW)("删除")])),_:2},1032,["onClick"]),(0,l.bF)(m,{type:"text",size:"small",onClick:a=>n.edit(e.row)},{default:(0,l.k6)((()=>[(0,l.eW)("编辑")])),_:2},1032,["onClick"])])),_:1})])),_:1},8,["data"]),(0,l.bF)(F,{title:"编辑学生信息",modelValue:d.dialogVisible,"onUpdate:modelValue":a[7]||(a[7]=e=>d.dialogVisible=e),width:"30%","before-close":n.handleClose},{default:(0,l.k6)((()=>[(0,l.bF)(u,{model:d.editForm},{default:(0,l.k6)((()=>[(0,l.bF)(r,{label:"学号"},{default:(0,l.k6)((()=>[(0,l.bF)(i,{modelValue:d.editForm.sno,"onUpdate:modelValue":a[1]||(a[1]=e=>d.editForm.sno=e),disabled:""},null,8,["modelValue"])])),_:1}),(0,l.bF)(r,{label:"姓名"},{default:(0,l.k6)((()=>[(0,l.bF)(i,{modelValue:d.editForm.name,"onUpdate:modelValue":a[2]||(a[2]=e=>d.editForm.name=e)},null,8,["modelValue"])])),_:1}),(0,l.bF)(r,{label:"性别"},{default:(0,l.k6)((()=>[(0,l.bF)(g,{modelValue:d.editForm.sex,"onUpdate:modelValue":a[3]||(a[3]=e=>d.editForm.sex=e),placeholder:"请选择性别"},{default:(0,l.k6)((()=>[(0,l.bF)(b,{label:"男",value:"男"}),(0,l.bF)(b,{label:"女",value:"女"})])),_:1},8,["modelValue"])])),_:1}),(0,l.bF)(r,{label:"年龄"},{default:(0,l.k6)((()=>[(0,l.bF)(i,{modelValue:d.editForm.age,"onUpdate:modelValue":a[4]||(a[4]=e=>d.editForm.age=e)},null,8,["modelValue"])])),_:1}),(0,l.bF)(r,{label:"班级"},{default:(0,l.k6)((()=>[(0,l.bF)(g,{modelValue:d.editForm.class,"onUpdate:modelValue":a[5]||(a[5]=e=>d.editForm.class=e),placeholder:"请选择班级"},{default:(0,l.k6)((()=>[((0,l.uX)(!0),(0,l.CE)(l.FK,null,(0,l.pI)(d.classOptions,(e=>((0,l.uX)(),(0,l.Wv)(b,{key:e[0],label:e[0],value:e[0]},null,8,["label","value"])))),128))])),_:1},8,["modelValue"])])),_:1})])),_:1},8,["model"]),(0,l.Lk)("span",s,[(0,l.bF)(m,{onClick:a[6]||(a[6]=e=>d.dialogVisible=!1)},{default:(0,l.k6)((()=>[(0,l.eW)("取消")])),_:1}),(0,l.bF)(m,{type:"primary",onClick:n.saveEdit},{default:(0,l.k6)((()=>[(0,l.eW)("保存")])),_:1},8,["onClick"])])])),_:1},8,["modelValue","before-close"])])}t(4603),t(7566),t(8721);var d={data(){return{tableData:[],sno:"",dialogVisible:!1,editForm:{sno:"",name:"",sex:"",age:"",class:""},classOptions:[]}},methods:{edit(e){this.editForm={...e},this.dialogVisible=!0,this.fetchClassOptions()},saveEdit(){let e=new URLSearchParams;e.append("sno",this.editForm.sno),e.append("name",this.editForm.name),e.append("sex",this.editForm.sex),e.append("age",this.editForm.age),e.append("class",this.editForm.class),this.$axios({method:"post",url:"http://127.0.0.1:8690/updatestudent",data:e,headers:{"Content-Type":"application/x-www-form-urlencoded;charset=UTF-8"}}).then((e=>{if(console.log(e.data),"successfully"==e.data.message){this.$message({type:"success",message:"操作成功!"}),this.dialogVisible=!1;let e=new URLSearchParams;this.$axios({method:"post",url:"http://127.0.0.1:8690/studentinfo",data:e,headers:{"Content-Type":"application/x-www-form-urlencoded;charset=UTF-8"}}).then((e=>{console.log(e.data),this.tableData=e.data.map((e=>({sno:e[0],name:e[1],sex:e[2],age:e[3],class:e[6]})))})).catch((e=>{console.error("请求失败:",e)}))}else this.$message({type:"warning",message:"操作失败!"})})).catch((e=>{console.error("请求失败:",e)}))},fetchClassOptions(){this.$axios({method:"post",url:"http://127.0.0.1:8690/classnum",headers:{"Content-Type":"application/x-www-form-urlencoded;charset=UTF-8"}}).then((e=>{console.log(e.data),this.classOptions=e.data})).catch((e=>{console.error("请求失败:",e)}))},confirmRemove(e){this.$confirm(`此操作将永久删除学生 ${e.name}，是否继续？`,"提示",{confirmButtonText:"确定",cancelButtonText:"取消",type:"warning"}).then((()=>{this.remove(e)})).catch((()=>{this.$message({type:"info",message:"已取消删除"})}))},remove(e){let a=new URLSearchParams;a.append("sno",e.sno),this.$axios({method:"post",url:"http://127.0.0.1:8690/reamovestudent",data:a,headers:{"Content-Type":"application/x-www-form-urlencoded;charset=UTF-8"}}).then((e=>{console.log(e.data),this.query(),this.$message({type:"success",message:"删除成功!"})})).catch((e=>{console.error("请求失败:",e),this.$message({type:"warning",message:"删除失败!"})}))},query(){if(!this.sno)return void this.$message({type:"warning",message:"请输入学号"});let e=new URLSearchParams;e.append("sno",this.sno),this.$axios({method:"post",url:"http://127.0.0.1:8690/querystudent",data:e,headers:{"Content-Type":"application/x-www-form-urlencoded;charset=UTF-8"}}).then((e=>{console.log(e.data),this.tableData=[{sno:e.data[0],name:e.data[1],sex:e.data[2],age:e.data[3],class:e.data[6]}],this.$message({type:"success",message:"查询成功!"})})).catch((e=>{console.error("请求失败:",e),this.$message({type:"warning",message:"查询失败!"})}))},handleClose(e){this.dialogVisible=!1}},mounted(){let e=new URLSearchParams;this.$axios({method:"post",url:"http://127.0.0.1:8690/studentinfo",data:e,headers:{"Content-Type":"application/x-www-form-urlencoded;charset=UTF-8"}}).then((e=>{console.log(e.data),this.tableData=e.data.map((e=>({sno:e[0],name:e[1],sex:e[2],age:e[3],class:e[6]})))})).catch((e=>{console.error("请求失败:",e)}))}},n=t(1241);const i=(0,n.A)(d,[["render",o]]);var r=i}}]);
//# sourceMappingURL=333.e3943a46.js.map