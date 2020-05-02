import {ApiResource, ApiResponse} from '../models/api.models';


export interface ApiSerializer {
  fromApiResponse(apiResponse: ApiResponse): ApiResource;
  toApiResponse(apiResource: ApiResource): ApiResponse;
}
