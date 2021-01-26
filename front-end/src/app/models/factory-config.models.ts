import {ApiResource} from './api.models';

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
