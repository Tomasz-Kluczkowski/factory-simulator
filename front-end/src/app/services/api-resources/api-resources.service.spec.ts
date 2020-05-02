import { TestBed } from '@angular/core/testing';

import { ApiResourcesService } from './api-resources.service';

describe('ApiResourcesService', () => {
  let service: ApiResourcesService<string>;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ApiResourcesService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
