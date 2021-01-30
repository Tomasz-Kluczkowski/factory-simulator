import {TestBed} from '@angular/core/testing';

import {FactoryConfigAPIService} from './factory-config-api.service';
import {HttpClientTestingModule, HttpTestingController} from '@angular/common/http/testing';
import {FactoryConfigAPIResource} from '../../../models/factory-config.models';
import {environment} from '../../../../environments/environment';
import {ApiEndpoints} from '../../../configuration/api-endpoints';

describe('FactoryConfigService', () => {
  let service: FactoryConfigAPIService;
  let backend: HttpTestingController;
  let mockFactoryConfigAPIResources: FactoryConfigAPIResource[];

  beforeEach(() => {
    TestBed.configureTestingModule(
      {
        imports: [HttpClientTestingModule],
      }
    );
    service = TestBed.inject(FactoryConfigAPIService);
    backend = TestBed.inject(HttpTestingController);

  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  it('should get the list of factory configs', () => {
    mockFactoryConfigAPIResources = [
      {
        id: 1,
        materials: ['A', 'B'],
        productCode: 'P',
        emptyCode: 'E',
        numberOfSimulationSteps: 10,
        numberOfConveyorBeltSlots: 3,
        numberOfWorkerPairs: 2,
        pickupTime: 5,
        dropTime: 2,
        buildTime: 1,
      },
      {
        id: 2,
        materials: ['C', 'D', 'E'],
        productCode: 'P1',
        emptyCode: 'E1',
        numberOfSimulationSteps: 101,
        numberOfConveyorBeltSlots: 31,
        numberOfWorkerPairs: 21,
        pickupTime: 51,
        dropTime: 21,
        buildTime: 11,
      }
    ];

    service.list().subscribe(factoryConfigs => {
      expect(factoryConfigs).toEqual(mockFactoryConfigAPIResources);
    });

    backend.expectOne({
      method: 'GET',
      url: `${environment.apiURL}/${ApiEndpoints.FACTORY_CONFIGS}`
    }).flush(mockFactoryConfigAPIResources);
  });
});

