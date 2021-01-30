import {ApiResource} from './api.models';
import {FactoryConfigAPIResource} from './factory-config.models';
import {ResultAPIResource} from './result.models';

export interface SimulationAPIResource extends ApiResource {
  name: string;
  description: string;
  start: string;
  stop: string;
  factoryConfigs?: FactoryConfigAPIResource[];
  results?: ResultAPIResource[];
}
