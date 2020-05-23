import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {HomeComponent} from './components/home/home.component';
import {PageNotFoundComponent} from './components/page-not-found/page-not-found.component';
import {PathResolveService} from './services/path-resolve/path-resolve.service';
import {paths} from './configuration/app-paths';


const routes: Routes = [
  {
    path: '',
    redirectTo: paths.home,
    pathMatch: 'full'
  },
  {
    path: paths.home,
    component: HomeComponent,
  },
  {
    path: '**',
    resolve: {
      path: PathResolveService
    },
    component: PageNotFoundComponent,
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
