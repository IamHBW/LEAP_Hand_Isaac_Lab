# --------------------------------------------------------
# LEAP Hand: Newton backend configuration for Isaac Lab 3.x
# --------------------------------------------------------

from isaaclab_newton.physics import MJWarpSolverCfg, NewtonCfg

import isaaclab.sim as sim_utils
from isaaclab.assets import ArticulationCfg, RigidObjectCfg
from isaaclab.envs import DirectRLEnvCfg, ViewerCfg
from isaaclab.markers import VisualizationMarkersCfg
from isaaclab.scene import InteractiveSceneCfg
from isaaclab.sim import SimulationCfg
from isaaclab.sim.spawners.materials.physics_materials_cfg import RigidBodyMaterialCfg
from isaaclab.utils import configclass
from isaaclab.utils.assets import ISAAC_NUCLEUS_DIR

from LEAP_Isaaclab.assets import LEAP_HAND_CFG


@configclass
class LeapHandEnvNewtonCfg(DirectRLEnvCfg):
    decimation = 4
    min_episode_length_s = 20.0
    episode_length_s = 120.0
    action_space = 16
    hist_len = 3
    store_cur_actions = True
    observation_space = 96
    state_space = 0
    viewer: ViewerCfg = ViewerCfg()
    viewer.eye = (0, 0, 2)

    solver_cfg = MJWarpSolverCfg(
        solver="newton",
        integrator="implicitfast",
        njmax=80,
        nconmax=70,
        impratio=10.0,
        cone="elliptic",
        update_data_interval=2,
        iterations=100,
        ls_iterations=15,
        ls_parallel=False,
        ccd_iterations=35,
    )
    newton_cfg = NewtonCfg(
        solver_cfg=solver_cfg,
        num_substeps=2,
        debug_mode=False,
    )
    sim: SimulationCfg = SimulationCfg(
        dt=1 / 120,
        render_interval=decimation,
        physics_material=RigidBodyMaterialCfg(
            static_friction=1.0,
            dynamic_friction=1.0,
        ),
        physics=newton_cfg,
    )

    robot_cfg: ArticulationCfg = ArticulationCfg(
        prim_path="/World/envs/env_.*/Robot",
        spawn=sim_utils.UsdFileCfg(
            usd_path=LEAP_HAND_CFG.spawn.usd_path,
            activate_contact_sensors=False,
        ),
        init_state=LEAP_HAND_CFG.init_state,
        actuators=LEAP_HAND_CFG.actuators,
        soft_joint_pos_limit_factor=LEAP_HAND_CFG.soft_joint_pos_limit_factor,
    )
    actuated_joint_names = [
        "a_0", "a_1", "a_2", "a_3", "a_4", "a_5", "a_6", "a_7",
        "a_8", "a_9", "a_10", "a_11", "a_12", "a_13", "a_14", "a_15",
    ]
    fingertip_body_names = ["fingertip", "thumb_fingertip", "fingertip_2", "fingertip_3"]

    object_cfg: RigidObjectCfg = RigidObjectCfg(
        prim_path="/World/envs/env_.*/object",
        spawn=sim_utils.UsdFileCfg(
            usd_path=f"{ISAAC_NUCLEUS_DIR}/Props/Blocks/DexCube/dex_cube_instanceable.usd",
            rigid_props=sim_utils.RigidBodyPropertiesCfg(
                kinematic_enabled=False,
                disable_gravity=False,
                enable_gyroscopic_forces=True,
                solver_position_iteration_count=8,
                solver_velocity_iteration_count=0,
                sleep_threshold=0.005,
                stabilization_threshold=0.0025,
                max_depenetration_velocity=1000.0,
            ),
            mass_props=sim_utils.MassPropertiesCfg(density=400.0),
            scale=(1.2, 1.2, 1.2),
        ),
        init_state=RigidObjectCfg.InitialStateCfg(pos=(-0.00, -0.1, 0.56), rot=(1.0, 0.0, 0.0, 0.0)),
    )
    goal_object_cfg: VisualizationMarkersCfg = VisualizationMarkersCfg(
        prim_path="/Visuals/goal_marker",
        markers={
            "goal": sim_utils.UsdFileCfg(
                usd_path=f"{ISAAC_NUCLEUS_DIR}/Props/Blocks/DexCube/dex_cube_instanceable.usd",
                scale=(1.2, 1.2, 1.2),
            )
        },
    )

    scene: InteractiveSceneCfg = InteractiveSceneCfg(num_envs=2048, env_spacing=0.75, replicate_physics=False)
    z_rotation_steps = 16
    dist_reward_scale = -10.0
    rot_reward_scale = 1.0
    rot_eps = 0.1
    action_penalty_scale = -0.0002
    torque_penalty_scale = -0.0
    pose_diff_penalty_scale = -0.3
    reach_goal_bonus = 250
    fall_penalty = -10
    fall_dist = 0.07
    success_tolerance = 0.2
    av_factor = 0.1
    action_type = "relative"
    act_moving_average = 1.0 / 24

    enable_adr = False
    events = None

    def __post_init__(self):
        super().__post_init__()
        if self.enable_adr:
            raise NotImplementedError("Newton backend does not support ADR in this environment yet.")
