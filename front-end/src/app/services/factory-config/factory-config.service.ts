import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {ApiResourcesService} from '../api-resources/api-resources.service';
import {FactoryConfigSerializer} from '../../serializers/factory-config.serializer';
import {FactoryConfigAPIResource} from '../../models/factory-config.models';


@Injectable({
  providedIn: 'root'
})
export class FactoryConfigService extends ApiResourcesService<FactoryConfigAPIResource> {

  constructor(httpClient: HttpClient) {
    super(
      httpClient,
      'api/factory-configs/',
      new FactoryConfigSerializer()
    );
  }
}
