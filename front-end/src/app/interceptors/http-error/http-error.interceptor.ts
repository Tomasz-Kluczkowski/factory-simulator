import { Injectable } from '@angular/core';
import {
  HttpRequest,
  HttpHandler,
  HttpEvent,
  HttpInterceptor, HttpErrorResponse
} from '@angular/common/http';
import {Observable, throwError} from 'rxjs';
import {ErrorDialogService} from '../../services/error-dialog/error-dialog.service';
import {catchError} from 'rxjs/operators';
import {HttpErrorData} from '../../models/error.models';

@Injectable()
export class HttpErrorInterceptor implements HttpInterceptor {

  constructor(public errorDialogService: ErrorDialogService) {}

  intercept(request: HttpRequest<unknown>, next: HttpHandler): Observable<HttpEvent<unknown>> {
    return next.handle(request).pipe(
      catchError((error: HttpErrorResponse) => {
        const data: HttpErrorData = {
          message: error.message,
          name: error.name,
          reason: error && error.error && error.error.reason ? error.error.reason : '',
          status: error.status,
          statusText: error.statusText,
          url: error.url
        };
        this.errorDialogService.openDialog(data);
        return throwError(error);
      })
    );
  }
}
