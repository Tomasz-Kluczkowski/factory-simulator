import {ApiResource, ApiResponse} from './api.models';

export interface FactoryConfigAPIResponse extends ApiResponse {
  materials: string[];
  product_code: string;
  empty_code: string;
  number_of_simulation_steps: number;
  number_of_conveyor_belt_slots: number;
  number_of_worker_pairs: number;
  pickup_time: number;
  drop_time: number;
  build_time: number;
}

export interface FactoryConfigAPIResource extends ApiResource {
  materials: string[];
  productCode: string;
  emptyCode: string;
  numberOfSimulationSteps: number;
  numberOfConveyorBeltSlots: number;
  numberOfWorkerPairs: number;
  pickupTime: number;
  dropTime: number;
  buildTime: number;
}
