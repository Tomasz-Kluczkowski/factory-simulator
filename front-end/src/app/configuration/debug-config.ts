import {environment} from '../../environments/environment';
import {HTTP_INTERCEPTORS} from '@angular/common/http';
import {HttpErrorInterceptor} from '../interceptors/http-error/http-error.interceptor';

export const DEV_PROVIDERS = [];
if (environment.debug) {
  console.log('Adding dev only providers');
  DEV_PROVIDERS.push(
    {provide: HTTP_INTERCEPTORS, useClass: HttpErrorInterceptor, multi: true}
  );
}
