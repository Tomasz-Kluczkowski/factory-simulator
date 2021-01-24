import {ApiSerializer} from './api.serializer';
import {FactoryConfigAPIResource, FactoryConfigAPIResponse} from '../models/factory-config.models';

export class FactoryConfigSerializer implements ApiSerializer {
  fromApiResponse(apiResponse: FactoryConfigAPIResponse): FactoryConfigAPIResource {
    return {
      id: apiResponse.id,
      materials: apiResponse.materials,
      productCode: apiResponse.product_code,
      emptyCode: apiResponse.empty_code,
      numberOfSimulationSteps: apiResponse.number_of_simulation_steps,
      numberOfConveyorBeltSlots: apiResponse.number_of_conveyor_belt_slots,
      numberOfWorkerPairs: apiResponse.number_of_worker_pairs,
      pickupTime: apiResponse.pickup_time,
      dropTime: apiResponse.drop_time,
      buildTime: apiResponse.build_time
    };
  }

  toApiResponse(apiResource: FactoryConfigAPIResource): FactoryConfigAPIResponse {
    return {
      id: apiResource.id,
      materials: apiResource.materials,
      product_code: apiResource.productCode,
      empty_code: apiResource.emptyCode,
      number_of_simulation_steps: apiResource.numberOfSimulationSteps,
      number_of_conveyor_belt_slots: apiResource.numberOfConveyorBeltSlots,
      number_of_worker_pairs: apiResource.numberOfWorkerPairs,
      pickup_time: apiResource.pickupTime,
      drop_time: apiResource.dropTime,
      build_time: apiResource.buildTime
    };
  }
}
