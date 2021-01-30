import { TestBed } from '@angular/core/testing';

import { SimulationAPIService } from './simulation-api.service';

describe('SimulationService', () => {
  let service: SimulationAPIService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(SimulationAPIService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
