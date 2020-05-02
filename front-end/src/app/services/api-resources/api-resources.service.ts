import {environment} from '../../../environments/environment';
import {HttpClient} from '@angular/common/http';
import {ApiSerializer} from '../../serializers/api.serializer';
import {Observable} from 'rxjs';
import {RequestOptions} from '../../models/api.models';
import {map} from 'rxjs/operators';


const API_URL = environment.apiURL;


export class ApiResourcesService<T> {

  constructor(
    private httpClient: HttpClient,
    private endpoint: string,
    private serializer: ApiSerializer,
    private url: string = API_URL,
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
