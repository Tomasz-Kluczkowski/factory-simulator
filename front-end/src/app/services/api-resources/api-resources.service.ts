import {environment} from '../../../environments/environment';
import {HttpClient} from '@angular/common/http';
import {ApiSerializer} from '../../serializers/api.serializer';
import {Observable} from 'rxjs';
import {ApiResource, RequestOptions} from '../../models/api.models';
import {map} from 'rxjs/operators';


const API_URL = environment.apiURL;


export abstract class ApiResourcesService<T extends ApiResource> {

  protected constructor(
    protected httpClient: HttpClient,
    protected endpoint: string,
    protected serializer: ApiSerializer,
    protected url: string = API_URL,
  ) { }

  list(requestOptions?: RequestOptions): Observable<T[]> {
    return this.httpClient
      .get(this.getUrl(this.endpoint), requestOptions)
      .pipe(
        map(
          (apiResponse: any) => apiResponse.map(apiResponseItem => this.serializer.fromApiResponse(apiResponseItem))
        )
      );
  }

  create(data: any, requestOptions?: RequestOptions): Observable<T> {
    return this.httpClient
      .post(this.getUrl(this.endpoint), this.serializer.toApiResponse(data), requestOptions)
      .pipe(
        map(
          (apiResponse: any) => {
            return <T>this.serializer.fromApiResponse(apiResponse);
          })
        )
  }

  getUrl(endpoint: string, id: any = ''): string {
    const idSuffix: string = id ? `${id}/` : '';
    return `${this.url}/${this.endpoint}${idSuffix}`;
  }
}
