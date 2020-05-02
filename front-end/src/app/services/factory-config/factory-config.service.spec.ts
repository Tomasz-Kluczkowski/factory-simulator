import { TestBed } from '@angular/core/testing';

import { FactoryConfigService } from './factory-config.service';

describe('FactoryConfigService', () => {
  let service: FactoryConfigService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(FactoryConfigService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
