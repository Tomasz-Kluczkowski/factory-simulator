import {HttpHeaders, HttpParams} from '@angular/common/http';

export interface ApiResponse {
  id: number;
}


export interface ApiResource {
  id: number;
}


export interface RequestOptions {
    headers?: HttpHeaders | {[header: string]: string | string[]};
    observe?: any;
    params?: HttpParams|{[param: string]: string | string[]};
    reportProgress?: boolean;
    responseType?: any;
    withCredentials?: boolean;
}
