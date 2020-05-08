import {environment} from '../../../environments/environment';
import {HttpClient} from '@angular/common/http';
import {ApiSerializer} from '../../serializers/api.serializer';
import {Observable} from 'rxjs';
import {RequestOptions} from '../../models/api.models';
import {map} from 'rxjs/operators';


const API_URL = environment.apiURL;


export abstract class ApiResourcesService<T> {

  protected constructor(
    protected httpClient: HttpClient,
    protected endpoint: string,
    protected serializer: ApiSerializer,
    protected url: string = API_URL,
  ) { }

  list(requestOptions?: RequestOptions): Observable<T[]> {
    return this.httpClient
      .get(`${this.url}/${this.endpoint}`, requestOptions)
      .pipe(
        map(
          (apiData: any) => apiData.map(apiResponse => this.serializer.fromApiResponse(apiResponse))
        )
      );
  }
}
