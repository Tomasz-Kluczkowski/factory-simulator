import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';

import {AppRoutingModule} from './modules/app-routing.module';
import {AppComponent} from './app.component';
import {HTTP_INTERCEPTORS, HttpClientModule} from '@angular/common/http';
import {PageNotFoundComponent} from './components/page-not-found/page-not-found.component';
import {HomeComponent} from './components/home/home.component';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {FlexLayoutModule} from '@angular/flex-layout';
import { NavigationComponent } from './components/navigation/navigation.component';
import {MaterialModule} from './modules/material.module';
import {AboutComponent} from './components/about/about.component';
import { ContactComponent } from './components/contact/contact.component';
import { SimulationComponent } from './components/simulation/simulation.component';
import { SimulationListViewComponent } from './components/simulation/simulation-list-view/simulation-list-view.component';
import { SimulationDetailViewComponent } from './components/simulation/simulation-detail-view/simulation-detail-view.component';
import { SimulationCreateViewComponent } from './components/simulation/simulation-create-view/simulation-create-view.component';
import {ReactiveFormsModule} from '@angular/forms';
import { ErrorDialogComponent } from './components/error-dialog/error-dialog/error-dialog.component';
import {HttpErrorInterceptor} from './interceptors/http-error/http-error.interceptor';

@NgModule({
  declarations: [
    AppComponent,
    PageNotFoundComponent,
    HomeComponent,
    NavigationComponent,
    AboutComponent,
    ContactComponent,
    SimulationComponent,
    SimulationListViewComponent,
    SimulationDetailViewComponent,
    SimulationCreateViewComponent,
    ErrorDialogComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    BrowserAnimationsModule,
    FlexLayoutModule,
    MaterialModule,
    ReactiveFormsModule,
  ],
  providers: [
    {provide: HTTP_INTERCEPTORS, useClass: HttpErrorInterceptor, multi: true}
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
