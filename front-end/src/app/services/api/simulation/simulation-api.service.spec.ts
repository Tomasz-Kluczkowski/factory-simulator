import {TestBed} from '@angular/core/testing';

import {SimulationAPIService} from './simulation-api.service';
import {HttpClientTestingModule, HttpTestingController} from '@angular/common/http/testing';
import {environment} from '../../../../environments/environment';
import {ApiEndpoints} from '../../../configuration/api-endpoints';
import {SimulationAPIResource} from '../../../models/simulation.models';

describe('SimulationService', () => {
  let service: SimulationAPIService;
  let backend: HttpTestingController;
  let mockSimulationAPIResources: SimulationAPIResource[];


  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
    });
    service = TestBed.inject(SimulationAPIService);
    backend = TestBed.inject(HttpTestingController);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  it('should get the list of simulations', () => {
    mockSimulationAPIResources = [
      {
        id: 1,
        name: 'simulation 1',
        description: 'some experiment',
        start: '2021-01-27T12:00:00Z',
        stop: '2021-01-27T13:00:00Z',
        factoryConfigs: [],
        results: [],
      },
      {
        id: 2,
        name: 'simulation 2',
        description: 'some new experiment',
        start: '2021-11-27T12:00:00Z',
        stop: '2021-11-27T13:00:00Z',
        factoryConfigs: [],
        results: [],
      }
    ];

    service.list().subscribe(factoryConfigs => {
      expect(factoryConfigs).toEqual(mockSimulationAPIResources);
    });

    backend.expectOne({
      method: 'GET',
      url: `${environment.apiURL}/${ApiEndpoints.SIMULATIONS}`
    }).flush(mockSimulationAPIResources);
  });

});
