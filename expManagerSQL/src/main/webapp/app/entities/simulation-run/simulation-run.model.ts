import { BaseEntity } from './../../shared';

export class SimulationRun implements BaseEntity {
    constructor(
        public id?: number,
        public simulationTrial?: string,
        public index?: number,
        public team_id?: number,
        public score?: number,
        public teamCapture?: number,
        public nonTeamCapture?: number,
        public job_num?: number,
        public task_num?: number,
        public results_dir?: string,
        public num_rows?: number,
        public align_weight_t_1?: number,
        public avoid_nonteam_weight_t_1?: number,
        public avoid_team_weight_t_1?: number,
        public centroid_weight_t_1?: number,
        public comms_range_t_1?: number,
        public fov_az_t_1?: number,
        public fov_el_t_1?: number,
        public goal_weight_t_1?: number,
        public max_pred_speed_t_1?: number,
        public max_speed_t_1?: number,
        public sphere_of_influence_t_1?: number,
        public motion_model_t_1?: string,
        public vel_max_t_1?: number,
        public motion_model_predator?: string,
        public pitch_rate_max_predator?: number,
        public turn_rate_max_predator?: number,
        public vel_max_predator?: number,
        public align_weight_t_2_predator?: number,
        public allow_prey_switching_t_2_predator?: boolean,
        public autonomy_t_2_predator?: string,
        public avoid_nonteam_weight_t_2_predator?: number,
        public avoid_team_weight_t_2_predator?: number,
        public capture_range_t_2_predator?: number,
        public centroid_weight_t_2_predator?: number,
        public comms_range_t_2_predator?: number,
        public max_pred_speed_t_2_predator?: number,
        public max_speed_t_2_predator?: number,
        public align_weight_t_3_predator?: number,
        public allow_prey_switching_t_3_predator?: boolean,
        public autonomy_t_3_predator?: string,
        public avoid_nonteam_weight_t_3_predator?: number,
        public avoid_team_weight_t_3_predator?: number,
        public capture_range_t_3_predator?: number,
        public centroid_weight_t_3_predator?: number,
        public comms_range_t_3_predator?: number,
        public max_pred_speed_t_3_predator?: number,
        public max_speed_t_3_predator?: number,
    ) {
        this.allow_prey_switching_t_2_predator = false;
        this.allow_prey_switching_t_3_predator = false;
    }
}
