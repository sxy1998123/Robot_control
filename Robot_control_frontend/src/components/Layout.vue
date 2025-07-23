<template>
  <div class="layout">
    <div class="form">
      <el-card class="box-card">
        <div class="card-body">
          <el-form ref="form" :model="form_params" label-width="140px" size="medium">
            <span class="title">参数输入:</span>
            <el-form-item label="机械臂1IP地址" size="medium">
              <el-input v-model="form_params.arm1_ip"></el-input>
            </el-form-item>
            <el-form-item label="机械臂2IP地址" size="medium">
              <el-input v-model="form_params.arm2_ip"></el-input>
            </el-form-item>
            <el-form-item label="是否开启末端设备" size="medium">
              <el-switch v-model="form_params.is_end_device"></el-switch>
            </el-form-item>
            <el-form-item label="末端设备名称" size="medium">
              <el-input v-model="form_params.end_device_name"></el-input>
            </el-form-item>
            <el-form-item label="机械臂项目文件路径" size="medium">
              <el-input v-model="form_params.arm_file_path"></el-input>
            </el-form-item>
            <el-form-item label="视觉项目文件路径" size="medium">
              <el-input v-model="form_params.vision_pro_file_path"></el-input>
            </el-form-item>
            <el-form-item label="初始位姿保存文件名" size="medium">
              <el-input v-model="form_params.init_pose_file_name"></el-input>
            </el-form-item>
            <el-form-item label="路点保存文件名" size="medium">
              <el-input v-model="form_params.waypoints_file_name"></el-input>
            </el-form-item>
          </el-form>
        </div>
      </el-card>
    </div>
    <div class="main">
      <el-card>
        <div class="btns-container">
          <span class="title">功能区:</span>
          <el-row :gutter="20">
            <el-col :span="6">
              <div class="grid-content bg-purple">
                <el-button type="primary" @click="handleClick('start_arm')" size="medium">启动机械臂</el-button>
              </div>
            </el-col>
            <el-col :span="6">
              <div class="grid-content bg-purple">
                <el-button type="primary" @click="handleClick('btn')" size="medium">机械臂位姿初始化</el-button>
              </div>
            </el-col>
            <el-col :span="6">
              <div class="grid-content bg-purple">
                <el-button type="primary" @click="handleClick('btn')" size="medium">取打磨工具</el-button>
              </div>
            </el-col>
            <el-col :span="6">
              <div class="grid-content bg-purple">
                <el-button type="primary" @click="handleClick('btn')" size="medium">切换机械臂模型1</el-button>
              </div>
            </el-col>
          </el-row>
          <el-row :gutter="20">
            <el-col :span="6">
              <div class="grid-content bg-purple">
                <el-button type="primary" @click="handleClick('btn')" size="medium">开启线夹位姿估计</el-button>
              </div>
            </el-col>
            <el-col :span="6">
              <div class="grid-content bg-purple">
                <el-button type="primary" @click="handleClick('btn')" size="medium">开启圆孔位姿估计</el-button>
              </div>
            </el-col>
            <el-col :span="6">
              <div class="grid-content bg-purple">
                <el-button type="primary" @click="handleClick('btn')" size="medium">取导电涂抹工具</el-button>
              </div>
            </el-col>
            <el-col :span="6">
              <div class="grid-content bg-purple">
                <el-button type="primary" @click="handleClick('btn')" size="medium">切换机械臂模型2</el-button>
              </div>
            </el-col>
          </el-row>
          <el-row :gutter="20">
            <el-col :span="6">
              <div class="grid-content bg-purple">
                <el-button type="primary" @click="handleClick('btn')" size="medium">发布线夹位姿</el-button>
              </div>
            </el-col>
            <el-col :span="6">
              <div class="grid-content bg-purple">
                <el-button type="primary" @click="handleClick('btn')" size="medium">运动到孔的位置</el-button>
              </div>
            </el-col>
            <el-col :span="6">
              <div class="grid-content bg-purple">
                <el-button type="primary" @click="handleClick('btn')" size="medium">取螺栓螺母旋紧工具</el-button>
              </div>
            </el-col>
            <el-col :span="6">
              <div class="grid-content bg-purple">
                <el-button type="primary" @click="handleClick('btn')" size="medium">切换机械臂模型3</el-button>
              </div>
            </el-col>
          </el-row>
          <el-row :gutter="20">
            <el-col :span="6">
              <div class="grid-content bg-purple">
                <el-button type="primary" @click="handleClick('btn')" size="medium">运动到线夹正前方</el-button>
              </div>
            </el-col>
            <el-col :span="6">
              <div class="grid-content bg-purple">
                <el-button type="primary" @click="handleClick('btn')" size="medium">线夹抓握姿态估计</el-button>
              </div>
            </el-col>
            <el-col :span="6">
              <div class="grid-content bg-purple">
                <el-button type="primary" @click="handleClick('btn')" size="medium">机械臂2抓握</el-button>
              </div>
            </el-col>
            <el-col :span="6">
              <div class="grid-content bg-purple">
                <el-button type="primary" @click="handleClick('btn')" size="medium">路点采集示数</el-button>
              </div>
            </el-col>
          </el-row>
          <el-row :gutter="20">
            <el-col :span="6">
              <div class="grid-content bg-purple">
                <el-button type="primary" @click="handleClick('btn')" size="medium">初始化位姿记录</el-button>
              </div>
            </el-col>
            <el-col :span="6">
              <div class="grid-content bg-purple">
                <el-button type="primary" @click="handleClick('btn')" size="medium">开启相机</el-button>
              </div>
            </el-col>
          </el-row>
        </div>
      </el-card>
    </div>
    <div class="aside">
      <el-card>
        <el-form ref="form" :model="form_params" label-width="140px" size="medium">
          <span class="form-title">参数输入:</span>
          <el-form-item label="机械臂1IP地址" size="medium">
            <el-input v-model="form_params.arm1_ip"></el-input>
          </el-form-item>
          <el-form-item label="机械臂2IP地址" size="medium">
            <el-input v-model="form_params.arm2_ip"></el-input>
          </el-form-item>
          <el-form-item label="是否开启末端设备" size="medium">
            <el-switch v-model="form_params.is_end_device"></el-switch>
          </el-form-item>
          <el-form-item label="末端设备名称" size="medium">
            <el-input v-model="form_params.end_device_name"></el-input>
          </el-form-item>
          <el-form-item label="机械臂项目文件路径" size="medium">
            <el-input v-model="form_params.arm_file_path"></el-input>
          </el-form-item>
          <el-form-item label="视觉项目文件路径" size="medium">
            <el-input v-model="form_params.vision_pro_file_path"></el-input>
          </el-form-item>
          <el-form-item label="初始位姿保存文件名" size="medium">
            <el-input v-model="form_params.init_pose_file_name"></el-input>
          </el-form-item>
          <el-form-item label="路点保存文件名" size="medium">
            <el-input v-model="form_params.waypoints_file_name"></el-input>
          </el-form-item>
        </el-form>
      </el-card>
    </div>
  </div>
</template>

<script>
import services from '@/services/api'

export default {
  name: 'layout',
  data() {
    return {
      form_params: {
        arm1_ip: '',
        arm2_ip: '',
        is_end_device: false,
        end_device_name: '',
        arm_file_path: '',
        vision_pro_file_path: '',
        init_pose_file_name: '',
        waypoints_file_name: ''
      }
    }
  },
  components: {

  },
  methods: {
    async handleClick(btn_name) {
      try {
        const data = {
          btn_name,
          form:this.form_params
        }
        console.log(btn_name)
        const resp = await services.test(data)
        console.log(resp.data)
        if (resp.data.code === 200) {
          this.$message.success("操作成功")
        } else {
          this.$message.error(resp.data.msg)
        }
      } catch (error) {
        console.log(error)
      }
    }
  }
}
</script>

<style lang="less" scoped>
// deep selector is used to override element-ui styles
// /deep/ .el-card__body {
//   padding: 0;
// }

::-webkit-scrollbar {
  width: 6px;
  height: 6px;
}

::-webkit-scrollbar-track-piece {
  background-color: transparent;
  -webkit-border-radius: 3px;
}

::-webkit-scrollbar-thumb:vertical {
  height: 6px;
  background-color: #D0D0D0;
  -webkit-border-radius: 3px;
}

::-webkit-scrollbar-thumb:horizontal {
  width: 6px;
  background-color: #D0D0D0;
  -webkit-border-radius: 3px;
}

::-webkit-scrollbar-thumb:vertical:hover,
::-webkit-scrollbar-thumb:horizontal:hover {
  background-color: #D0D0D0;
}


.form-title {
  font-weight: 600;
  font-size: 18px;
  color: #303133;

}

.title {
  font-weight: 600;
  font-size: 18px;
  color: #303133;
}

.el-form {
  border: 1px solid #ccc;
  box-sizing: border-box;
  border-radius: 4px;
  padding: 12px;
  margin-bottom: 12px;
  text-align: left;

  .btns {
    text-align: right;
  }

  .el-form-item {
    margin-bottom: 12px;

    &:first-of-type {
      margin-top: 12px;
    }
  }
}

.layout {
  width: 100%;
  height: 100%;
  display: flex;

  .form {
    min-width: 320px;
    width: 30%;

    .el-card {
      height: 100%;
      box-sizing: border-box;
    }
  }

  .main {
    flex: 1;

    .el-card {
      height: 100%;
      box-sizing: border-box;

      .btns-container {
        border: 1px solid #ccc;
        border-radius: 4px;
        box-sizing: border-box;
        padding: 12px;
        margin-bottom: 12px;
        text-align: left;

        .el-row {
          margin-top: 12px;

          .el-button {
            width: 100%;
            height: 60px;
          }
        }
      }
    }
  }

  .aside {
    min-width: 320px;
    width: 30%;
    display: none;
    .el-card {
      height: 100%;
      box-sizing: border-box;
    }
  }
}
</style>
