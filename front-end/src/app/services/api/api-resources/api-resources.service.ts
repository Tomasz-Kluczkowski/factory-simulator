import {environment} from '../../../../environments/environment';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';
import {ApiResource, RequestOptions} from '../../../models/api.models';


const API_URL = environment.apiURL;


export abstract class ApiResourcesService<T extends ApiResource> {

  protected constructor(
    protected httpClient: HttpClient,
    protected endpoint: string,
    protected url: string = API_URL,
  ) { }

  get(id: number, requestOptions?: RequestOptions): Observable<T> {
    return this.httpClient.get<T>(this.getUrl(this.endpoint, id), requestOptions);
  }

  list(requestOptions?: RequestOptions): Observable<T[]> {
    return this.httpClient.get<T[]>(this.getUrl(this.endpoint), requestOptions);
  }

  create(data: T, requestOptions?: RequestOptions): Observable<T> {
    return this.httpClient.post<T>(this.getUrl(this.endpoint), data, requestOptions);
  }

  getUrl(endpoint: string, id: any = ''): string {
    const idSuffix: string = id ? `${id}/` : '';
    return `${this.url}/${this.endpoint}${idSuffix}`;
  }
}
