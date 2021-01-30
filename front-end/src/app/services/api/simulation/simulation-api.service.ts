import { Injectable } from '@angular/core';
import {ApiResourcesService} from '../api-resources/api-resources.service';
import {SimulationAPIResource} from '../../../models/simulation.models';
import {HttpClient} from '@angular/common/http';
import {ApiEndpoints} from '../../../configuration/api-endpoints';

@Injectable({
  providedIn: 'root'
})
export class SimulationAPIService extends ApiResourcesService<SimulationAPIResource> {

  constructor(httpClient: HttpClient) {
    super(httpClient, ApiEndpoints.SIMULATIONS)
  }
}
