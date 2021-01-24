import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {ApiResourcesService} from '../api-resources/api-resources.service';
import {FactoryConfigAPIResource} from '../../models/factory-config.models';
import {ApiEndpoints} from '../../configuration/api-endpoints';


@Injectable({
  providedIn: 'root'
})
export class FactoryConfigService extends ApiResourcesService<FactoryConfigAPIResource> {

  constructor(httpClient: HttpClient) {
    super(
      httpClient,
      ApiEndpoints.FACTORY_CONFIGS,
    );
  }
}
